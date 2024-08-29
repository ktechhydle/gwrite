from gwrite import GWritePrinter, GPos

printer = GWritePrinter()
printer.extrude(GPos(100, 10))
printer.generate('test.gcode')