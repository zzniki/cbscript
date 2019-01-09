class mock_mcfunction(object):
	def __init__(self):
		self.add_command_log = []
		
	def add_operation(self, selector, id1, operation, id2):
		None
		
	def add_command(self, command):
		self.add_command_log.append(command)
	
	def insert_command(self, command, index):
		None
		
	def get_utf8_text(self):
		return ''
		
	def defined_objectives(self):
		return {}
		
	def register_local(self, id):
		None
			
	def finalize(self):
		None
		
	def single_command(self):
		return None
			
	def check_single_entity(self, selector):
		return False
			
	def get_path(self, selector, var):
		None
				
	def set_path(self, selector, var):
		None

	def get_vector_path(self, selector, var, assignto):
		return True
			
	def set_vector_path(self, selector, var, values):
		return True
			
	def register_objective(self, objective):
		None
		
	def register_array(self, name, from_val, to_val):
		None

	def apply_replacements(self, text):
		None
		
	def register_block_tag(self, name, blocks):
		None
		
	def get_scale(self):
		return 1000
		
	def set_scale(self, scale):
		None
		
	scale = property(get_scale, set_scale)
	
	@property
	def arrays(self):
		return {}
		
	@property
	def block_tags(self):
		return {}

	@property
	def namespace(self):
		return 'test'
		
	@property
	def macros(self):
		return {}
		
	@property
	def template_functions(self):
		return {}
		
	@property
	def functions(self):
		return {}
		
	@property
	def selectors(self):
		return {}
	
	def get_scratch(self):
		return 'test_scratch'
		
	def free_scratch(self, id):
		None
		
	def apply_environment(self, text):
		return text
		
	def add_constant(self, val):
		return 'test_constant'
		
	def allocate_rand(self, val):
		None
		
	def get_friendly_name(self):
		return 'test_friendly_name'
		
	def get_random_objective(self):
		return 'test_random_objective'
		
	def register_function(self, name, func):
		None
		
	def get_unique_id(self):
		return 1
		
	def update_self_selector(self, selector):
		None
		
	def get_python_env(self):
		return {}
		
	def clone_environment(self):
		return None
		
	def get_combined_selector(self, selector):
		return selector
		
	def set_dollarid(self, id, val):
		None
		
	def set_atid(self, id, fullselector):
		None
		
	def push_environment(self, new_env):
		None
		
	def pop_environment(self):
		None		