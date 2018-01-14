PWD       = $(shell pwd)
SRC_DIR   = $(PWD)
SRC_CID   = $(SRC_DIR)/cidfont.ps

AFDKO_OTF=font_fdk.otf
AFDKO_TTF=font_fdk.ttf
AFDKO_TTF_HMTX_MODIFIED=font_fdk.hmtx_mod.ttf
TARGET_FEATURES  = $(SRC_DIR)/features
CID_FONTINFO = $(SRC_DIR)/cidfontinfo
FONT_MENU_NAME_DB = $(SRC_DIR)/FontMenuNameDB
TARGET_SEQUENCES = $(SRC_DIR)/sequences.txt

TX_DIR      = $(shell which tx)
FDK_DIR     = $(dir $(TX_DIR))/../..
CMAP        = "$(FDK_DIR)/Tools/SharedData/Adobe Cmaps/Adobe-Japan1/UniJIS-UTF32-H"
CID_CHARSET = "$(FDK_DIR)/Tools/SharedData/CID charsets/AJ16-J15"
LANG_GROUP  = "$(FDK_DIR)/Tools/SharedData/CID charsets/AJ16-J15.LanguageGroups"

OTF2TTF=../../../fonttools/Snippets/otf2ttf.py

autohint   ?=n

################################################################################

.PHONY: all
all: $(AFDKO_OTF) $(AFDKO_TTF) $(AFDKO_TTF_HEAD_MODIFIED) $(AFDKO_TTF_HMTX_MODIFIED)

$(AFDKO_OTF): $(SRC_CID)
	makeotf -f $< -o $@ -ff $(TARGET_FEATURES) -ch $(CMAP) -ci $(TARGET_SEQUENCES) -mf $(FONT_MENU_NAME_DB) -fi $(CID_FONTINFO) -r -nS 2>&1 | tee build.txt
	python -B rename_family.py -f "Source Han Sans FDK" $@

$(AFDKO_TTF): $(AFDKO_OTF)
	python -B $(OTF2TTF) -o $@ $<
	python -B rename_family.py -f "Source Han Sans FDK TT" $@

$(AFDKO_TTF_HMTX_MODIFIED): $(AFDKO_TTF)
	python -B update_ttf_hmtx.py -o $@ --vmtx $<

.PHONY: clean
clean:
	rm -rf $(AFDKO_OTF) $(AFDKO_TTF) $(AFDKO_TTF_HEAD_MODIFIED) $(AFDKO_TTF_HMTX_MODIFIED) current.fpr build.txt
