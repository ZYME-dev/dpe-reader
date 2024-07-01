#r "nuget: FSharp.Data, 6.4.0"
#r "nuget: System.Xml.XDocument, 4.3.0"
open FSharp.Data
open System.Xml.Linq

let filePath: string = "../assets/samples/2187E0981996L.xml"

let xd = XDocument.Load(filePath)
for d in xd.Descendants() do
    printfn $"{d.Value}"


type DPE = XmlProvider<Schema="../assets/schemas/DPEv2.3.xsd">
let model = DPE.Load(filePath)
// printfn $"version : {model.Administratif.Value.EnumVersionId}"
let murs = model.Dpe.Value.Logement.Value.Enveloppe.MurCollections
for mur in murs do
    printfn $"{mur.DonneeEntree.Value.Description}"
    printfn $"{mur.DonneeEntree.Value.SurfaceParoiOpaque} m²"

let count = Array.length murs
let surface_totale =  
    murs 
    |> Array.fold (fun acc mur -> acc + mur.DonneeEntree.Value.SurfaceParoiOpaque) 0.0
printfn $"surface totale = {surface_totale}"