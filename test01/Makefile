SRC_UFO=font.ufo
TARGET_OTF=master_otf/font.otf
TARGET_TTF=master_ttf/font.ttf

all: $(TARGET_OTF) $(TARGET_TTF)

$(TARGET_OTF): $(SRC_UFO)
	fontmake -o otf -u $<

$(TARGET_TTF): $(SRC_UFO)
	fontmake -o ttf -u $<

.PHONY: clean
clean:
	rm -rf master_otf master_ttf
