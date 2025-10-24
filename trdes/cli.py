
        from __future__ import annotations
        import argparse
        from pathlib import Path
        from .logging_config import configure_logging
        from .core.combine import combine_files
        from .core.split import split_by_lines
        from .core.search import search_tokens
        from .core.sortdemo import sort_lines
        from .core.weekday import weekday_of
        from .core.dates import add_days, range_days
        from .core.accum import accumulate
        from .core.parsecmd import render

        def main() -> None:
            parser = argparse.ArgumentParser(prog='trdes', description='Modern TRDES CLI (no .DAT/.MRS/barcode)')
            parser.add_argument('-v', '--verbose', action='count', default=0, help='Increase verbosity (-v, -vv)')
            sub = parser.add_subparsers(dest='cmd', required=True)

            p_comb = sub.add_parser('combine', help='Combine files under a directory')
            p_comb.add_argument('root', type=Path)
            p_comb.add_argument('--pattern', action='append', default=['*.txt'], help='Glob pattern(s)')
            p_comb.add_argument('--out', type=Path, required=True)
            p_comb.add_argument('--headers', action='store_true', help='Add file headers in output')

            p_split = sub.add_parser('split', help='Split a text file by number of lines')
            p_split.add_argument('src', type=Path)
            p_split.add_argument('--lines', type=int, default=1000)
            p_split.add_argument('--out', type=Path, default=Path('split_out'))

            p_search = sub.add_parser('search', help='Search tokens in files')
            p_search.add_argument('root', type=Path)
            p_search.add_argument('--pattern', action='append', default=['*.txt'])
            p_search.add_argument('--tokens', required=True, help='Comma-separated tokens')
            p_search.add_argument('--mode', choices=['any','all'], default='all')
            p_search.add_argument('--ignore-case', action='store_true')
            p_search.add_argument('--out', type=Path)

            p_sort = sub.add_parser('sort', help='Sort lines with options')
            p_sort.add_argument('src', type=Path)
            p_sort.add_argument('--out', type=Path)
            p_sort.add_argument('--unique', action='store_true')
            p_sort.add_argument('--numeric', action='store_true')
            p_sort.add_argument('--key-col', type=int)
            p_sort.add_argument('--delimiter', default=None)

            p_weekday = sub.add_parser('weekday', help='Show weekday for ISO date (YYYY-MM-DD)')
            p_weekday.add_argument('date')

            p_date = sub.add_parser('date', help='Date utilities')
            sub_date = p_date.add_subparsers(dest='dcmd', required=True)
            p_add = sub_date.add_parser('add', help='Add/sub days to date')
            p_add.add_argument('date')
            p_add.add_argument('--days', type=int, required=True)
            p_range = sub_date.add_parser('range', help='List inclusive range of dates')
            p_range.add_argument('start')
            p_range.add_argument('end')

            p_acc = sub.add_parser('accum', help='Accumulate numeric column, optional group by')
            p_acc.add_argument('src', type=Path)
            p_acc.add_argument('--value-col', type=int, required=True)
            p_acc.add_argument('--group-col', type=int)
            p_acc.add_argument('--delimiter', default=',')
            p_acc.add_argument('--out', type=Path)

            p_parse = sub.add_parser('parsecmd', help='Render a command template with variables {TOKEN}')
            p_parse.add_argument('template')
            p_parse.add_argument('--var', action='append', nargs=2, metavar=('KEY','VALUE'), default=[])

            args = parser.parse_args()
            configure_logging(args.verbose)

            if args.cmd == 'combine':
                count = combine_files(args.root, args.pattern, args.out, add_headers=args.headers)
                print(f"Wrote {args.out} with {count} lines")

            elif args.cmd == 'split':
                parts = split_by_lines(args.src, args.out, args.lines)
                for p in parts:
                    print(p)
                print(f"Created {len(parts)} parts in {args.out}")

            elif args.cmd == 'search':
                tokens = [t.strip() for t in args.tokens.split(',') if t.strip()]
                hits = search_tokens(args.root, args.pattern, tokens, mode=args.mode, ignore_case=args.ignore_case)
                text = ''.join(hits)
                if args.out:
                    args.out.write_text(text, encoding='utf-8')
                    print(f"Wrote results to {args.out} ({len(hits)} hits)")
                else:
                    print(text, end='')

            elif args.cmd == 'sort':
                sort_lines(args.src, args.out, unique=args.unique, numeric=args.numeric,
                           key_col=args.key_col, delimiter=args.delimiter)
                if args.out:
                    print(f"Wrote sorted lines to {args.out}")

            elif args.cmd == 'weekday':
                print(weekday_of(args.date))

            elif args.cmd == 'date':
                if args.dcmd == 'add':
                    print(add_days(args.date, args.days))
                elif args.dcmd == 'range':
                    for d in range_days(args.start, args.end):
                        print(d)

            elif args.cmd == 'accum':
                rows = accumulate(args.src, args.value_col, group_col=args.group_col, delimiter=args.delimiter)
                out_lines = [f"{k},{v}" for k,v in rows]
                txt = "
".join(out_lines) + "
"
                if args.out:
                    args.out.write_text(txt, encoding='utf-8')
                    print(f"Wrote {args.out}")
                else:
                    print(txt, end='')

            elif args.cmd == 'parsecmd':
                vars_map = {k:v for k,v in args.var}
                print(render(args.template, vars_map))

        if __name__ == '__main__':
            main()
