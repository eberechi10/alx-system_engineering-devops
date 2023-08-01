#!/usr/bin/env ruby
# regular expression to only match capital letters
puts ARGV[0].scan(/[A-Z]/).join
