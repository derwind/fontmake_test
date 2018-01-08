SRC_UFO=font.ufo
TARGET_OTF=master_otf/font.otf
TARGET_TTF=master_ttf/font.ttf
AFDKO_OTF=font_fdk.otf
AFDKO_TTF=font_fdk.ttf
AFDKO_TTF_HEAD_MODIFIED=font_fdk.head_mod.ttf

OTF2TTF=../../../fonttools/Snippets/otf2ttf.py

all: $(TARGET_OTF) $(TARGET_TTF) $(AFDKO_OTF) $(AFDKO_TTF) $(AFDKO_TTF_HEAD_MODIFIED)

$(TARGET_OTF): $(SRC_UFO)
	fontmake -o otf -u $< --production-names --keep-overlaps

$(TARGET_TTF): $(SRC_UFO)
	fontmake -o ttf -u $< --production-names --keep-overlaps

$(AFDKO_OTF): $(SRC_UFO)
	makeotf -f $< -o $@

$(AFDKO_TTF): $(AFDKO_OTF)
	python -B $(OTF2TTF) -o $@ $<

$(AFDKO_TTF_HEAD_MODIFIED): $(AFDKO_TTF)
	python -B update_flags.py -o $@ $<

.PHONY: clean
clean:
	rm -rf master_otf master_ttf $(AFDKO_OTF) $(AFDKO_TTF) $(AFDKO_TTF_HEAD_MODIFIED) current.fpr
