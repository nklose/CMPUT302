APP = basicgame

include $(SDK_DIR)/Makefile.defs

OBJS = \
	$(ASSETS).gen.o \
	SensorListener.o \
	text.o \
	loader.o \
	main.o
	
ASSETDEPS += assets/*.png $(ASSETS).lua
CDEPS += *.h

include $(SDK_DIR)/Makefile.rules
