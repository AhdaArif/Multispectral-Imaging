#define OFS 0x20

#define PIN *(volatile unsigned char *)(OFS + 0x16)
#define DDR *(volatile unsigned char *)(OFS + 0x17)
#define PRT *(volatile unsigned char *)(OFS + 0x18)