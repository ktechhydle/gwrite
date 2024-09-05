from src import GWritePrinter, GWriteFilament, GPos

filament = GWriteFilament(200, 60)  # PLA

printer = GWritePrinter()
printer.createPurgeLine(filament, levelBed=True)

# optional: send gcode to printer via usb
printer.sendCodeToPrinter(baudrate=115200)  # baudrate is found on your printer (default is 115200)
