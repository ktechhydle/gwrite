# GWrite
***A simple way to generate 3d Printer GCODE files in Python***

### With GWrite, you can:
- Generate GCODE files by specifying easy functions
- Send GCODE to your printer via a USB port
- Control temperatures and filaments
- And more!

### Install

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
