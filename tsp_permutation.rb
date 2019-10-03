module TSP

  private
  @@data_set = []
  @@shortest_path = []
  @@shortest_weight = 99999999999

  def self.process
    n = @@data_set.length
    (1..n-1).to_a.permutation.each do |possible_path|
      possible_path.unshift 0
      possible_path.push 0
      path_weight = 0
      possible_path.each_with_index do |current_node, i|
        if i != possible_path.length-1
          path_weight += @@data_set[current_node][possible_path[i+1]]
        end
      end
      if path_weight < @@shortest_weight
        @@shortest_weight = path_weight
        @@shortest_path = possible_path
      end
    end
  end

  def self.validate_data_set(data)
    if !(data.class == Array && data[0].class == Array)
      raise 'Invalid data-set, should be a square matrix'
    end
  end

  public 
  def self.init_data_set(data)
    validate_data_set(data)
    @@data_set = data
    process
    {
      path: @@shortest_path,
      weight: @@shortest_weight
    }
  end

end

# a = [
#   [0, 10, 15, 20, 10, 15, 5, 3, 10, 15],
#   [10, 0, 35, 25, 10, 15, 20, 4, 10, 15],
#   [15, 35, 0, 30, 10, 5, 20, 12, 10, 15],
#   [20, 25, 30, 0, 10, 15, 20, 23, 10, 15],
#   [10, 0, 35, 25, 10, 15, 20, 11, 10, 15],
#   [15, 5, 0, 30, 10, 15, 20, 21, 10, 15],
#   [10, 0, 35, 25, 10, 15, 20, 22, 10, 15],
#   [15, 35, 0, 30, 10, 5, 20, 9, 10, 15],
#   [10, 0, 35, 5, 10, 15, 20, 11, 10, 15],
#   [15, 35, 0, 30, 10, 5, 20, 21, 10, 15]
# ]

# https://www.geeksforgeeks.org/travelling-salesman-problem-set-1/
a = [
  [0,10,15,20],
  [10,0,35,25],
  [15,35,0,30],
  [20,15, 30,0]
  ]

puts TSP.init_data_set(a)
#output
#{:path=>[0, 6, 1, 7, 2, 5, 8, 3, 9, 4, 0], :weight=>64}
