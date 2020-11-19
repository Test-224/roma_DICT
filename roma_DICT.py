#!/usr/bin/env python3

from argparse import ArgumentParser


a_to_z = (
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n',
	'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z'
	 )

boin = ('a', 'i', 'u', 'e', 'o')

err_words = (
	'bc', 'bd', 'bg', 'bj', 'bm', 'bn', 'br', 'bs', 'bt', 'bw', 'bz', 'bf', 'bp', 'bv', 'bk',
	'cb', 'cc', 'cd', 'cg', 'cj', 'cm', 'cn', 'cr', 'cs', 'ct', 'cw', 'cz', 'cf', 'cp', 'cv', 'cy', 'ck',
	'db', 'dc', 'dg', 'dh', 'dj', 'dm', 'dn', 'dr', 'ds', 'dt', 'dw', 'dz', 'df', 'dp', 'dv', 'dk',
	'gb', 'gc', 'gd', 'gh', 'gj', 'gm', 'gn', 'gr', 'gs', 'gt', 'gw', 'gz', 'gf', 'gp', 'gv', 'gk',
	'hb', 'hc', 'hd', 'hg', 'hj', 'hm', 'hn', 'hr', 'hs', 'ht', 'hw', 'hz', 'hf', 'hp', 'hv', 'hk',
	'jb', 'jc', 'jd', 'jg', 'jh', 'jm', 'jn', 'jr', 'js', 'jt', 'jw', 'jz', 'jf', 'jp', 'jv', 'jk',
	'kb', 'kc', 'kd', 'kg', 'kh', 'kj', 'km', 'kn', 'kr', 'ks', 'kt', 'kw', 'kz', 'kf', 'kp', 'kv',
	'mb', 'mc', 'md', 'mg', 'mh', 'mj', 'mn', 'mr', 'ms', 'mt', 'mw', 'mz', 'mf', 'mp', 'mv', 'mk',
	'sb', 'sc', 'sd', 'sg', 'sj', 'sm', 'sn', 'sr', 'st', 'sw', 'sz', 'sf', 'sp', 'sv', 'sk',
	'tb', 'tc', 'td', 'tg', 'th', 'tj', 'tm', 'tn', 'tr', 'tw', 'tz', 'tf', 'tp', 'tv', 'tk',
	'wb', 'wc', 'wd', 'wg', 'wh', 'wj', 'wm', 'wn', 'wr', 'ws', 'wt', 'wz', 'wf', 'wp', 'wv', 'wy', 'wk',
	'yb', 'yc', 'yd', 'yg', 'yh', 'yj', 'ym', 'yn', 'yr', 'ys', 'yt', 'yw', 'yz', 'yf', 'yp', 'yv', 'yk',
	'zb', 'zc', 'zd', 'zg', 'zh', 'zj', 'zm', 'zn', 'zr', 'zs', 'zt', 'zw', 'zf', 'zp', 'zv', 'zk',
	'fb', 'fc', 'fd', 'fg', 'fj', 'lm', 'fn', 'fr', 'fs', 'ft', 'fw', 'fz', 'fp', 'fv', 'fk',
	'pb', 'pc', 'pd', 'pg', 'pj', 'lm', 'pn', 'pr', 'ps', 'pt', 'pw', 'pz', 'pf', 'pv', 'pk',
	'rb', 'rc', 'rd', 'rg', 'rj', 'lm', 'rn', 'rs', 'rt', 'rw', 'rz', 'rf', 'rp', 'rv', 'rk',
	'vb', 'vc', 'vd', 'vg', 'vj', 'lm', 'vn', 'vs', 'vt', 'vw', 'vz', 'vf', 'vp', 'vy', 'vk',
	)


def roma_DICT(dict_size):

	def roma_DICTi(word, depth, dict_size, index):

		if depth == dict_size:
			yield word
			return

		for chara in a_to_z:
			if chara in boin:
				# 発音できない
				if index == 1 and word[-1:] not in ('k', 'c', 's', 't', 'n', 'h', 'm', 'y', 'r', 'f', 'b', 'p', 'v', 'w', 'g', 'j', 'd', 'z'):
					continue

				for roma in roma_DICTi(word + chara, depth + 1, dict_size, 0):
					yield roma
			else:
				# 末尾に子音はおかしい (けど、'ん' だけは例外)
				if depth == dict_size - 1 and not chara == 'n':
					continue
				# 発音できない組み合せ
				elif index == 1 and (word[-1:] + chara) in err_words:
					continue
				# 'rakkyo' みたいなケース
				elif index == 2 and chara == 'y':
					if word[-2:] not in ('kk', 'ss', 'tt', 'nn', 'hh', 'mm', 'rr'):
						continue
				# これ以上子音は連続できない
				elif index >= 2:
					continue

				for roma in roma_DICTi(word + chara, depth + 1, dict_size, index + 1):
					yield roma

	assert dict_size > 0

	for chara in a_to_z:
		for roma in roma_DICTi(chara, 1, dict_size, 0 if chara in boin else 1):
			yield roma


if __name__ == '__main__':

	parser = ArgumentParser()
	parser.add_argument('-s', '--size', type=int, default=3)
	args = parser.parse_args()

	for roma in roma_DICT(args.size):
		print(roma)

