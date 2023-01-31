#!/usr/bin/env ruby
puts ARGV[0].scan(/(\[from:([a-zA-Z]+|\+?\w+)).+(\[to:)([a-zA-Z]+|\+?\w+).+(\[flags):(.\w+.+-1)\]/).join(",")
