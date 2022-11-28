//
//  ContentView.swift
//  TEST
//
//  Created by 乔炳赫 on 2022/9/24.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        HStack {
            VStack {
                Image(systemName: "globe")
                    .imageScale(.large)
                    .foregroundColor(.accentColor)
                Text("Hello, world!")
                Image(systemName: "lasso")
                    .imageScale(.medium)
                    .foregroundColor(.accentColor)
            }
            Image(systemName: "pencil.tip.crop.circle")
                .imageScale(.medium)
                .foregroundColor(.accentColor)
                .padding()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
