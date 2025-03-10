# Box Breathing App

A minimalist desktop application for practicing box breathing (also known as square breathing or four-square breathing), a powerful relaxation technique used to reduce stress and improve focus.

## Features

- **Clean, Minimalist Interface**: Distraction-free design focused on the breathing exercise
- **Visual Countdown**: Clear, large numbers guide you through each phase
- **Audio Feedback**: Gentle beep signals phase transitions
- **Customizable Breathing Durations**: Personalize each phase duration (Inhale, Hold, Exhale, Hold)
- **Always-On-Top Option**: Pin the window to keep it visible over other applications
- **Draggable Window**: Position the app anywhere on your screen
- **10-Minute Sessions**: Structured breathing sessions with automatic timing

## Breathing Pattern

The app guides you through a customizable box breathing pattern:
1. **Inhale**: Default 4 seconds (customizable)
2. **Hold**: Default 4 seconds (customizable)
3. **Exhale**: Default 8 seconds (customizable)
4. **Hold**: Default 4 seconds (customizable, can be set to 0 to skip)

This pattern repeats for 10 minutes, helping you maintain a consistent breathing rhythm.

## How to Use

1. **Launch**: Run `BoxBreath_v1.1.exe`
2. **Customize (Optional)**: Adjust the duration for each breathing phase using the input fields
3. **Position**: Drag the window to your preferred location on screen
4. **Pin (Optional)**: Click the 📌 icon to keep the window always on top
5. **Start**: Click the "START" button to begin your breathing session
6. **Follow**: Watch the countdown and follow the breathing instructions
7. **Audio**: Listen for the beep that signals phase transitions
8. **Stop**: Click "STOP" to end the session early, or let it complete the 10-minute cycle

## Controls

- **📌 Button**: Toggle always-on-top mode
- **✕ Button**: Close the application
- **START/STOP Button**: Begin or end a breathing session
- **Title Bar**: Click and drag to move the window

## Technical Details

- **Language**: Python 3.12
- **GUI Framework**: Tkinter
- **Sound System**: Windows winsound module
- **Distribution**: Single executable file (created with PyInstaller)

## Installation

No installation required! Simply download and run `BoxBreath_v1.1.exe`. The application is portable and can run on any Windows system without additional dependencies.

## Development

If you want to run from source or modify the code:

1. Ensure Python 3.12 or later is installed
2. Clone the repository
3. Install PyInstaller (if you want to build the executable):
   ```
   pip install pyinstaller
   ```
4. Run from source:
   ```
   python box_breathing_app.py
   ```
5. Build executable:
   ```
   pyinstaller --noconsole --onefile box_breathing_app.py
   ```

## License

This project is open-source and available for personal and commercial use.

## Credits

Developed as a minimalist breathing exercise tool with focus on simplicity and effectiveness.
