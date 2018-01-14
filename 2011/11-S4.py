import sys
on, op, an, ap, bn, bp, abn, abp = map(int, sys.stdin.readline().split())
on_, op_, an_, ap_, bn_, bp_, abn_, abp_ = map(int, sys.stdin.readline().split())
blood = 0


def transfer(x, x_):
    global blood
    if x > x_:
        blood += x_
        return x - x_, 0
    else:
        blood += x
        return 0, x_ - x

abn, abn_ = transfer(abn, abn_)
abn, abp_ = transfer(abn, abp_)
abp, abp_ = transfer(abp, abp_)

an, an_ = transfer(an, an_)
bn, bn_ = transfer(bn, bn_)

ap, ap_ = transfer(ap, ap_)
bp, bp_ = transfer(bp, bp_)
ap, abp_ = transfer(ap, abp_)
bp, abp_ = transfer(bp, abp_)

an, ap_ = transfer(an, ap_)
bn, bp_ = transfer(bn, bp_)
an, abn_ = transfer(an, abn_)
bn, abn_ = transfer(bn, abn_)
an, abp_ = transfer(an, abp_)
bn, abp_ = transfer(bn, abp_)

on, on_ = transfer(on, on_)
on, abn_ = transfer(on, abn_)
op, op_ = transfer(op, op_)
on, op_ = transfer(on, op_)
op, ap_ = transfer(op, ap_)
op, bp_ = transfer(op, bp_)
op, abp_ = transfer(op, abp_)
on, an_ = transfer(on, an_)
on, bn_ = transfer(on, bn_)
on, ap_ = transfer(on, ap_)
on, bp_ = transfer(on, bp_)
on, abp_ = transfer(on, abp_)

print(blood)








