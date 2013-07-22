let smallsrc = " |> (fun x-> printfn \"%A%s\" x <| System.String.Join(\"\", Array.map char x))"
printfn "%A%s" (Array.map int <| smallsrc.ToCharArray()) smallsrc
