from gwrite import GWritePrinter, GWriteFilament, GPos

filament = GWriteFilament(200, 60)  # PLA

printer = GWritePrinter()
printer.homePrinter() # home all axis
printer.prepareFor(filament)  # prepare printer for filament (heat up to PLA temperatures)
printer.extrude(GPos(100, 1000))  # extrude 100mm of filament at 1000mm/min
printer.generate('test.gcode')
