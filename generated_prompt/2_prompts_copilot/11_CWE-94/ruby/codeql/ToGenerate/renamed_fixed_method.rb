# Uses `define_method` instead of constructing a string
module GoodMakeGetter
  def self.create_class_with_getter(method_name, return_value)
    new_class = Class.new

    end
    new_class
  end
end
two = GoodMakeGetter.create_class_with_getter(:two, "bar")
puts "Two is #{two.new.two}"
