# SideBySide

![Blender](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Blender_logo_no_text.svg/1024px-Blender_logo_no_text.svg.png)

SideBySide is a Blender 4.5 addon for macOS that allows launching multiple independent Blender application instances — either blank new windows or specific `.blend` files — to enable true side-by-side editing without replacing existing open files.

## Features

- Open a brand new empty Blender instance.
- Open any `.blend` file in a new Blender instance.
- Each instance runs as a separate macOS application process.
- Avoids default Blender macOS limitation where opening a new file replaces the current one.
- Keyboard shortcuts on macOS:
  - **Command + Option + N**: Open new blank instance.
  - **Command + Shift + Option + N**: Open .blend file in new instance.

## Installation

1. Download or clone this repository.
2. In Blender 4.5, go to **Edit → Preferences → Add-ons → Install**.
3. Select the addon `.py` file and enable it.
4. Use the new menu entries under **File** or the keyboard shortcuts.

## Usage

- **File > Open New Blank Blender Instance:** Opens an empty new Blender window.
- **File > Open Blender File in New Instance:** Opens a file browser to select a `.blend` file, then opens it in a new Blender window.

## Requirements

- Blender 4.5 or newer.
- macOS with Blender installed in `/Applications/Blender.app`.

## Notes

- If Blender is installed elsewhere, update the `BLENDER_PATH` in the addon script accordingly.
- This addon does not change how macOS or Finder open Blender files by default.
- Designed to solve Blender’s single-instance limitation on macOS by launching multiple app processes.

## License

This addon is licensed under the [GNU General Public License v3](LICENSE).

## Author

tank shield
