int get_int_at_offset(int offset) {
  int values[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
  int *values_ptr = values;
  // GOOD: the offset is automatically scaled by sizeof(int).
  return *(values_ptr + offset);
}
