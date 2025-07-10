void good_server() {
  char* query = getenv("QUERY_STRING");
  const char* html_prefix = "<p>Query results for ";
  puts(html_prefix);

