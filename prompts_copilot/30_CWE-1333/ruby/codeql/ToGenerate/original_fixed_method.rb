class UsersController < ActionController::Base
  def example
    #
    # This method is an example of how to handle user input safely
    param = params[:user_input]
    sanitized_param = sanitize(param)
    # Use sanitized_param in a safe context
  end
#