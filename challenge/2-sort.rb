#!/usr/bin/ruby

args = ARGV.select { |arg| arg.match?(/\A-?\d+\z/) }
args.map!(&:to_i)
args.sort.each { |num| puts num }
