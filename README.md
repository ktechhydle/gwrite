# GWrite
***A simple way to interact with your 3d Printer using GCODE in Python***

### With GWrite, you can:
- Generate GCODE files by specifying easy functions
- Send GCODE to your printer via a USB port
- Load GCODE files into your printer
- Control temperatures and filaments
- And more!

### Install

### Types
- `GWritePrinter()`: the base class for all functions and methods
- `GWriteFilament(extruderTemp: int, heatbedTemp: int)`: a class for describing a filament and its attributes (used for preparing printer temperatures)
- `GPos(pos: float, speed: float)`: a class for describing positions and speeds (primarily used for moving axis)

### All Functions (GWritePrinter)
| Command                                                                   | Purpose                                                                                                         | Actual GCODE                                        |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| `homeAxis(axis)`                                                          | Home the specified axis                                                                                         | `G28 [X, Y, Z]`                                     |
| `homePrinter()`                                                           | Home all axis                                                                                                   | `G28`                                               |
| `levelBed()`                                                              | Perform mesh bed leveling (if supported by your printer)                                                        | `G29`                                               |
| `setAbsoluteMode()`                                                       | Set coordinates to absolute mode                                                                                | `G90`                                               |
| `setRelativeMode()`                                                       | Set coordinates to relative mode                                                                                | `G91`                                               |
| `setX(pos: GPos)`                                                         | Move x axis to the specified position                                                                           | `G1 X[pos] F[speed]`                                |
| `setY(pos: GPos)`                                                         | Move y axis to the specified position                                                                           | `G1 Y[pos] F[speed]`                                |
| `setZ(pos: GPos)`                                                         | Move z axis to the specified position                                                                           | `G1 Z[pos] F[speed]`                                |
| `move(self, axis, pos: GPos)`                                             | Move the specified axis to a specified position                                                                 | `G1 [axis][pos] F[speed]`                           |
| `heatExtruderToTemp(temp: int)`                                           | Set extruder temperature                                                                                        | `M104 S[temp]`                                      |
| `heatBedToTemp(temp: int)`                                                | Set heatbed temperature                                                                                         | `M140 S[temp]`                                      |
| `prepareFor(filament: GWriteFilament)`                                    | Prepare for printing with specified filament                                                                    | `M104 S[extruderTemp]`<br>`M140 S[heatbedTemp]`     |
| `cooldown()`                                                              | Cooldown the hotend and heatbed, and turn on the part cooling fan to speed up cooling                           | uses internal functions                             |
| `extrude(amount: GPos)`                                                   | Extrude the specified amount                                                                                    | `G1 E[amount] F[speed]`                             |
| `turnFanOn()`                                                             | Turn the fan on                                                                                                 | `M106`                                              |
| `turnFanOff()`                                                            | Turn the fan off                                                                                                | `M107`                                              |
| `setFanTo(speed: int)`                                                    | Set the fan to a specific speed                                                                                 | `M106 S[speed]`                                     |
| `setFlowPercent(self, percent: int)`                                      | Set the flow percent                                                                                            | `M221 S[percent]`                                   |
| `setInputShaperFrequencies(self, xFrequency: int, yFrequency: int)`       | Set the input shaper frequencies for the X and Y axis (if supported by your printer)                            | `M593 X F[xFrequency]`<br/>`M593 Y F[yFrequency]`   |
| `autotunePID(pid, targetTemp: int)`                                       | Autotune the PID for the hotend or heatbed                                                                      | `M303 E0 S[targetTemp]`<br>`M303 E-1 S[targetTemp]` |
| `displayMessage(message: str, playTone=False)`                            | Display a message on the screen (if `playTone=True`, the printer will play a sound as the message is displayed) | `M117 [message]`                                    |
| `duration: int = 220, frequency: int = 440`                               | Play a tone with the specified frequency and duration                                                           | `M300 S[frequency] P[duration]`                     |
| `addCustomCommand(command: str)`                                          | Add a custom command to the GCODE list                                                                          | `[your command]`                                    |
| `addComment(comment: str)`                                                | Add a comment to the GCODE list                                                                                 | `; [your comment]`                                  |
| `createPurgeLine(self, filament: GWriteFilament, levelBed: bool = False)` | Create a purge line with the specified filament and optionally level the bed before doing so                    | uses internal functions                             |
| `storeSettings()`                                                         | Store the printer settings to EEPROM                                                                            | `M500`                                              |
| `disableMotors()`                                                         | Disable the stepper motors                                                                                      | `M18`                                               |
| `disableInputShaper()`                                                    | Disable input shaper (if supported by your printer)                                                             | `M593 F0`                                           |
| `generate(filename: str)`                                                 | Generate a GCODE file and save to the specified filename                                                        | File contents                                       |
| `loadCodeFromFile(filename: str)`                                         | Load GCODE from a file and replace current commands                                                             | File contents                                       |
| `sendCodeToPrinter(baudrate: int)`                                        | Send GCODE to the printer over serial                                                                           | Serial commands                                     |
| `clearCode()`                                                             | Clear all commands from the GCODE list                                                                          | (Cleared)                                           |

### Example Code
```
from gwrite import GWritePrinter, GWriteFilament, GPos

filament = GWriteFilament(200, 60)  # PLA

printer = GWritePrinter()
printer.homePrinter()  # home all axis
printer.levelBed()  # preform mesh bed levelling (if supported by your printer)
printer.turnFanOff()  # turn cooling fan off
printer.prepareFor(filament)  # prepare printer for filament (heat up to PLA temperatures)
printer.extrude(GPos(100, 1000))  # extrude 100mm of filament at 1000mm/min
printer.setZ(GPos(100, 1000))  # move z axis to 100mm at a speed of 1000mm/min
printer.addComment('This is a test file.')
printer.generate('test.gcode')  # write generated gcode to file
# optional: send gcode to printer via usb
printer.sendCodeToPrinter(baudrate=115200)  # baudrate is found on your printer (default is 115200)
```
