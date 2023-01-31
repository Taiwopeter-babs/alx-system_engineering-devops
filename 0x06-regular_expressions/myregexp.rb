#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:([a-zA-Z]+|\+?\d+)?\]\s(\[to:)([a-zA-Z]+|\+?\d+)?\]\s(\[flags):(.\w+.+-1)?\]/).join(",")
