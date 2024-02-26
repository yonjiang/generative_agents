

import os
work_dir = os.getcwd()

maze_assets_loc = work_dir+"/environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"



fs_storage = work_dir + "/environment/frontend_server/storage"
fs_temp_storage = work_dir + "/environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True