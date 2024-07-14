def test_bad_adjective_num():
    """bad_adjectives"""

    n = random.choice(range(-10, 0))
    rv, out = getstatusoutput(f'{prg} -a {n}')
    assert rv != 0
    assert re.search(f'--adjectives "{n}" must be > 0', out)
    return args.parse_args()
args = parser.parse_args()

if args.adjectives < 1:
    parser.error(f'--adjectives "{args.adjectives}" must be >0')
    return args

def main():
    args = get_args()
    random.seed(args.seed)