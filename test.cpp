const char *foo() {
    // \c is actually invalid; the rest are fine.
    return "foo \t bar \c baz \055 foo \x2D bar \n baz \0 foo";
}
