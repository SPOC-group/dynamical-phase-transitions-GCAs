from src.config import *
from src.backtracking_dynamic_cavity.fixed_point_iteration import rs_calculation
from src.backtracking_dynamic_cavity.fixed_point_iteration import population_dynamics
from src.backtracking_dynamic_cavity.initialization import init_balanced, init_random_Gauss
from utils.experiments import *

exp_name = f'example'
log_dir = RESULT_DIR / exp_name
log_dir.mkdir(exist_ok=True, parents=True)
its=2000
r = '001011'
c=1
p=1

res = rs_calculation(its=its, 
		    alpha=0.99, 
		    rule_code=r, 
		    c=c, 
		    d=len(r) - 1,
                     log_dir=log_dir, 
                     log_suffix=f'end',
                     mag_init_temp=0.0,
                     p=p,
                     fix_observable=None,
                     init_func=init_random_Gauss,
                     eps
                     )
dump_pickle({ **res}, log_dir / f'rs.its={its}.{r}.{p=}.{c=}.pkl')

print('**********')
print('RS entropy', res['entropy'])
print('**********')
