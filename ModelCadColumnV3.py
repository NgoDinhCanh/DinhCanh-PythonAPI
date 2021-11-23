# def GetAllFamilySymbol(family):
#     familySymbols = []
#     familySymbolIds = family.GetFamilySymbolIds()
#     for familySymbolId in familySymbolIds :
#         symbol = family.Document.GetElement(familySymbolId)
#         familySymbols.Add(symbol)
#     return familySymbols

def GetFamilySymbolColumn(family,b,h,bPara,hPara) :
    allFamilySymbol = family.GetAllFamilySymbol()
    bParameter = allFamilySymbol[0].LookupParameter(bPara)
    hParameter = allFamilySymbol[0].LookupParameter(hPara)
    if (bParameter == None & hParameter == None) :
        MessageBox.Show("Two parameters dimemsion of column family have to name is"
                                + bPara + hPara)
        return None
        # Tìm trong list type của Column đã có type với kích thước b, h chưa.
        # Nếu đã có thì lấy về type đó. chưa có thì tạo mới
    for symbol in allFamilySymbol:
        bParameter = symbol.LookupParameter(bPara)
        hParameter = symbol.LookupParameter(hPara)

        bvalue = Convert.ToDouble(bParameter.GetValue())
        hvalue = Convert.ToDouble(hParameter.GetValue())

        if (Math.Abs(bvalue - b) < 0.001 & Math.Abs(hvalue - h) < 0.001) :

            return symbol
        # // làm tròn đến hàng đơn vị, ví dụ: 2995.5 -> 2996
        # //double sectionX = Math.Round(DLQUnitUtils.FeetToMm(b), 0);
        # //double sectionY = Math.Round(DLQUnitUtils.FeetToMm(h), 0);
        # //string name = string.Concat(sectionX, "x", sectionY);

        newName = string.Concat(DLQUnitUtils.FeetToMm(b).ToString(), 
                "x", DLQUnitUtils.FeetToMm(h).ToString())

            # if (name.Equals("0x0")) return null;
            # if (name.Equals("0x0") || Math.Abs(sectionX) < 0.01 ||
            #     Math.Abs(sectionY) < 0.01) return null;

        result = None
        tx = Transaction(family.Document)    
        tx.Start("Create new Column Type")
        s1 = allFamilySymbol[0].Duplicate(newName)
        s1.LookupParameter(bPara).Set(b)
        s1.LookupParameter(hPara).Set(h)
        result.Add(s1)
        tx.Commit()        
    return result