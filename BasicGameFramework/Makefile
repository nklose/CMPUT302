APP = basicgame

include $(SDK_DIR)/Makefile.defs

OBJS = \
	$(ASSETS).gen.o \
	main.o \
	SensorListener.o \
	text.o
	
ASSETDEPS += *.png $(ASSETS).lua
CDEPS += *.h

include $(SDK_DIR)/Makefile.rules
