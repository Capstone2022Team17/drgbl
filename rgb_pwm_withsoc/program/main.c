
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <irq.h>
#include <uart.h>
#include <console.h>
#include <generated/csr.h>

static char *readstr(void)
{
	char c[2];
	static char s[64];
	static int ptr = 0;

	if(readchar_nonblock()) {
		c[0] = readchar();
		c[1] = 0;
		switch(c[0]) {
			case 0x7f:
			case 0x08:
				if(ptr > 0) {
					ptr--;
					putsnonl("\x08 \x08");
				}
				break;
			case 0x07:
				break;
			case '\r':
			case '\n':
				s[ptr] = 0x00;
				putsnonl("\n");
				ptr = 0;
				return s;
			default:
				if(ptr >= (sizeof(s) - 1))
					break;
				putsnonl(c);
				s[ptr] = c[0];
				ptr++;
				break;
		}
	}

	return NULL;
}

static char *get_token(char **str)
{
	char *c, *d;

	c = (char *)strchr(*str, ' ');
	if(c == NULL) {
		d = *str;
		*str = *str+strlen(*str);
		return d;
	}
	*c = 0;
	d = *str;
	*str = c+1;
	return d;
}

static void prompt(void)
{
	printf("COMMAND >> ");
}

static void help(void)
{
	puts("Available commands:");
	puts("rgb                             - test rgb");
    puts("help                            - display commands ");
	puts("reboot                          - Reboot SoC and CPU");
}

static void rgb(void)
{
    puts("execute rgb command here");
	printf("Before write rgb red read: %lx\n", rgbled_red_read());
    rgbled_red_write(0x1);
	printf("After write rgb red read: %lx\n", rgbled_red_read());
	printf("Before write rgb green read: %lx\n", rgbled_green_read());
    rgbled_green_write(0x1);
	printf("After write rgb green read: %lx\n", rgbled_green_read());
	printf("Before write rgb blue read: %lx\n", rgbled_blue_read());
    rgbled_blue_write(0x1);
	printf("After write rgb blue read: %lx\n", rgbled_blue_read());
}

static void reboot(void)
{
	ctrl_reset_write(1);
}

static void console_service(void)
{
	char *str;
	char *token;

	str = readstr();
	if(str == NULL) return;
	token = get_token(&str);
	if(strcmp(token, "help") == 0) {
		help();
    } else if (strcmp(token, "rgb") == 0) {
        rgb();
    } else if (strcmp(token, "reboot") == 0) {
        reboot();
    }
	prompt();
}

int main(void)
{
#ifdef CONFIG_CPU_HAS_INTERRUPT
	irq_setmask(0);
	irq_setie(1);
#endif
	uart_init();

	puts("\nRGB Test "__DATE__" "__TIME__"\n");
	help();
	prompt();

	while(1) {
		console_service();
	}

	return 0;
}