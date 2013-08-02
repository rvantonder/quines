cc() {
  printf("char " "s" "[]={");int i;for(i=0;i<sizeof(s);i++) {printf("%04#4x,", s[i]);}; printf("};\n"); 
  printf("char " "p" "[]={");int i;for(i=0;i<sizeof(p);i++) {printf("%04#4x,", p[i]);}; printf("};\n"); 
  printf("char " "c" "[]={");int i;for(i=0;i<sizeof(c);i++) {printf("%04#4x,", c[i]);}; printf("};\n"); 
  printf("char " "f" "[]={");int i;for(i=0;i<sizeof(f);i++) {printf("%04#4x,", f[i]);}; printf("};\n"); 
  printf("char " "l" "[]={");int i;for(i=0;i<sizeof(l);i++) {printf("%04#4x,", l[i]);}; printf("};\n"); 
  printf("char " "s" "[]={");int i;for(i=0;i<sizeof(s);i++) {putchar(a[i]);}; printf("};\n");;
}
int main (int argc, char *argv[]) {
if (argc >= 2 && strcmp (argv[1], "py") == 0)
  py();
else
  cc();
}
