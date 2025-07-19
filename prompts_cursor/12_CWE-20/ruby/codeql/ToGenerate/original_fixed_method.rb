# https://github.com/github/codeql/blob/main/ruby/ql/src/queries/security/cwe-020/examples/IncompleteUrlSubstringSanitization_GOOD.rb
class AppController < ApplicationController
    def index
        url = params[:url]
        host = URI(url).host
        #
        if host.nil?
            redirect_to url
        elsif host.include?("example.com")
#
            redirect_to url
        end
    end
end