const char *foo() {
    /* \c is actually invalid; the rest are fine.  */
    return "foo \t bar \c baz \055 foo \x2D bar \n baz \0 foo";
}

const char *tabs(int i) {
	if (i % 2 == 1)
		return "odd indented with tabs";
	else
		return "even indented with tabs";
}

const char *greeting() {
  return "Hello, world!\n";
}

const char *farewell() {
  return "Goodbye, world\n";
}
