PWD       = $(shell pwd)
SRC_DIR   = $(PWD)
SRC_CID   = $(SRC_DIR)/cidfont.ps
FONT_NAME = SourceHanSansJP-Regular

TARGET   = $(FONT_NAME).otf
TARGET_FEATURES  = $(SRC_DIR)/features
CID_FONTINFO = $(SRC_DIR)/cidfontinfo
FONT_MENU_NAME_DB = $(SRC_DIR)/FontMenuNameDB
TARGET_SEQUENCES = $(SRC_DIR)/sequences.txt

TX_DIR      = $(shell which tx)
FDK_DIR     = $(dir $(TX_DIR))/../..
CMAP        = "$(FDK_DIR)/Tools/SharedData/Adobe Cmaps/Adobe-Japan1/UniJIS-UTF32-H"
CID_CHARSET = "$(FDK_DIR)/Tools/SharedData/CID charsets/AJ16-J15"
LANG_GROUP  = "$(FDK_DIR)/Tools/SharedData/CID charsets/AJ16-J15.LanguageGroups"

autohint   ?=n

################################################################################

.PHONY: all
all: $(TARGET)

$(TARGET): $(SRC_CID)
	makeotf -f $< -o $@ -ff $(TARGET_FEATURES) -ch $(CMAP) -ci $(TARGET_SEQUENCES) -mf $(FONT_MENU_NAME_DB) -fi $(CID_FONTINFO) -r -nS 2>&1 | tee build.txt

.PHONY: clean
clean:
	rm -rf $(TARGET) current.fpr build.txt
