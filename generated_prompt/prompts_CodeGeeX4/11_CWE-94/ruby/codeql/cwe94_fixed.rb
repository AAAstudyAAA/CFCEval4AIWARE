# Uses `define_method` instead of constructing a string
module GoodMakeGetter
  def self.define_getter_class(getter_name, val)
    new_class = Class.new
    new_class.module_eval do
      define_method(getter_name) { val }
    end
    new_class
  end
end

two = GoodMakeGetter.define_getter_class(:two, "bar")
puts "Two is #{two.new.two}"



require 'json'

module BadMakeGetter
  # Makes a class with a method named `getter_name` that returns `val`
  def self.define_getter_class(getter_name, val)
    new_class = Class.new
    new_class.module_eval <<-END
      def #{getter_name}
        #{JSON.dump(val)}
      end
    END
    new_class
  end
end

one = BadMakeGetter.define_getter_class(:one, "foo")
puts "One is #{one.new.one}"