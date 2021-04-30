Option Explicit

Sub Nutirition_Project():
Dim r As Integer
Dim fat As Double
Dim carbs As Double
Dim protein As Double

 For r = 2 To Range("A2").End(xlDown).Row
    ' fat (%) = fat calories / total calories = (fat in grams * 9) / total calories
    fat = Round(Cells(r, 8).Value / Cells(r, 4).Value, 2)
    Cells(r, 5).Value = fat

    ' Carbs (%) = Carbs calories / total calories = (Carbs in grams * 4) / total calories
    carbs = Round(Cells(r, 13).Value / Cells(r, 4).Value, 2)
    Cells(r, 6).Value = carbs

    ' Protein (%) = Protein calories / total calories = (Protein in grams * 4) / total calories
    protein = Round(Cells(r, 16).Value / Cells(r, 4).Value, 2)
    Cells(r, 7).Value = protein
Next r
End Sub

    



