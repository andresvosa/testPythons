"""_summary_
"""
def prnt_mtrx(pmtrx):
    """_summary_

    Args:
        pmtrx (_type_): _description_
    """
    print()
    [print(rw) for rw in pmtrx]

def main():
    """Transpose matrix with no libraries
    """
    mtrx = [['O','O','O'],['','X','O'],['X','','O']]
    prnt_mtrx(mtrx)
    rmtrx = [list(_) for _ in zip(*mtrx)]
    prnt_mtrx(rmtrx)
    #Siin on variant list comprehensioniga
    #rmtrx_comp = [[mtrx[j][i] for j in range(len(mtrx))] for i in range(len(mtrx[0]))]0
    #prnt_mtrx(rmtrx_comp)


if __name__ == '__main__':
    main()
    