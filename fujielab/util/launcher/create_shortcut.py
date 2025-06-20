"""
Windows環境でのショートカット作成機能を提供するモジュール
"""

import os
import sys
import platform
from .i18n import tr
from .debug_util import error_print

# Windows環境でのショートカット作成に必要
if platform.system() == "Windows":
    try:
        import win32com.client
        import pythoncom

        HAS_WIN32COM = True
    except ImportError:
        HAS_WIN32COM = False
else:
    HAS_WIN32COM = False


def create_windows_shortcut():
    """
    Windows環境でデスクトップにショートカットを作成する関数

    Returns:
        bool: ショートカット作成の成否
    """
    if not HAS_WIN32COM:
        print(tr("Error: pywin32 package is required for creating shortcuts."))
        print(tr("Please install it using: pip install pywin32"))
        return False

    try:
        # ユーザーのデスクトップパスを取得
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        if not os.path.exists(desktop_path):
            # 日本語環境など、デスクトップパスが異なる場合のフォールバック
            desktop_path = os.path.join(os.path.expanduser("~"), "デスクトップ")
            if not os.path.exists(desktop_path):
                error_print(tr("Error: Could not find the Desktop folder."))
                return False

        # 実行ファイルのパスを取得
        pythonw_exe = sys.executable.replace("python.exe", "pythonw.exe")

        package_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(package_dir, "resources", "icon.ico")
        if not os.path.exists(icon_path):
            error_print(tr("Error: Icon file not found at {}").format(icon_path))
            icon_path = ""

        # ショートカットのパス
        shortcut_path = os.path.join(desktop_path, "Fujielab Launcher.lnk")

        # COM オブジェクトを作成
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)

        # ショートカットのプロパティを設定
        shortcut.TargetPath = pythonw_exe
        shortcut.Arguments = "-m fujielab.util.launcher.run"
        shortcut.WorkingDirectory = os.path.expanduser("~")
        if icon_path:
            shortcut.IconLocation = icon_path
        shortcut.Description = "Fujielab Utility Launcher"
        
        # 環境変数を確実に引き継ぐための設定
        # pythonw.exe はCOMオブジェクトを介して実行されるため環境変数が継承されにくい場合がある
        # shortcut.Hotkey = ""  # ホットキーが設定されている場合は削除
        # 現在のPATH環境変数を継承して正しくcondaなどを検出できるようにする

        # ショートカットを保存
        shortcut.Save()

        print(tr("Shortcut created successfully on the Desktop."))
        return True
    except Exception as e:
        print(tr("Error creating shortcut:"), str(e))
        return False


def create_macos_shortcut():
    """Create an Application bundle in ``~/Applications`` for macOS."""
    try:
        from pathlib import Path
        import shutil
        import subprocess

        app_dir = Path.home() / "Applications" / "Fujielab Launcher.app"
        contents = app_dir / "Contents"
        macos_dir = contents / "MacOS"
        resources_dir = contents / "Resources"

        if app_dir.exists():
            shutil.rmtree(app_dir)

        macos_dir.mkdir(parents=True)
        resources_dir.mkdir(parents=True)

        package_dir = os.path.dirname(os.path.abspath(__file__))
        icon_png = os.path.join(package_dir, "resources", "icon.png")
        icon_icns = resources_dir / "icon.icns"
        if os.path.exists(icon_png):
            try:
                subprocess.run([
                    "sips", "-s", "format", "icns", icon_png,
                    "--out", str(icon_icns)
                ], check=True)
            except Exception:
                shutil.copy(icon_png, resources_dir / "icon.png")

        info_plist = contents / "Info.plist"
        plist_content = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">
<plist version=\"1.0\">
<dict>
    <key>CFBundleName</key><string>Fujielab Launcher</string>
    <key>CFBundleIdentifier</key><string>com.fujielab.launcher</string>
    <key>CFBundleVersion</key><string>1.0</string>
    <key>CFBundleExecutable</key><string>run.sh</string>
    <key>CFBundleIconFile</key><string>{icon_icns.name if icon_icns.exists() else 'icon.png'}</string>
</dict>
</plist>
"""
        with open(info_plist, "w") as f:
            f.write(plist_content)

        run_sh = macos_dir / "run.sh"
        with open(run_sh, "w") as f:
            f.write(f"#!/bin/bash\n\"{sys.executable}\" -m fujielab.util.launcher.run \"$@\"\n")
        os.chmod(run_sh, 0o755)

        print(tr("Shortcut created successfully in the Applications folder."))
        return True
    except Exception as e:
        print(tr("Error creating shortcut:"), str(e))
        return False
