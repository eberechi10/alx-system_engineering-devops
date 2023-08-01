#!/usr/bin/env ruby
# regular expression to only match the case above
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
