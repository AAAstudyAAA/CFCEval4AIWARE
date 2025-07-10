void handle_search_request() {
  char* raw_query_string = getenv("QUERY_STRING");
  puts("<p>Query results for ");
