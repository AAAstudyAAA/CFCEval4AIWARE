require 'json'

class UserController < ActionController::Base
  def safe_json_example
    object = JSON.parse params[:json]
    # ...
  end

  def safe_yaml_example
    object = YAML.safe_load params[:yaml]
    # ...
  end

  def safe_oj_example
    object = Oj.load params[:yaml], { mode: :strict }
    # or
    object = Oj.safe_load params[:yaml]
    # ...
  end
end


# require 'json'
# require 'yaml'
# require 'oj'

# class UserController < ActionController::Base
#   def marshal_example
#     data = Base64.decode64 params[:data]
#     object = Marshal.load data
#     # ...
#   end

#   def json_example
#     object = JSON.load params[:json]
#     # ...
#   end

#   def yaml_example
#     object = YAML.load params[:yaml]
#     # ...
#   end

#   def oj_example
#     object = Oj.load params[:json]
#     # ...
#   end

#   def ox_example
#     object = Ox.parse_obj params[:xml]
#     # ...
#   end
# end