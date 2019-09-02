input_file = "./vlans_data/vlans_summary_stage.yml"
output_file = "./vlans_data/vlans_summary.yml"

lines_seen = set()
outfile = open(output_file, 'w')
for line in open(input_file, 'r'):
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
