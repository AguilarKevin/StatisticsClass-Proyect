from tkinter import ttk, END, messagebox, CENTER, Text

class FrameTab1(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        self.container = ttk.LabelFrame(self, text = 'medidas de dispersion y desviacion estandar')
        self.container.grid(row = 0, column = 0,sticky = "w,e,s,n", padx = 5, ipadx = 5)
        
        #Entries
        self.containerEntries = ttk.LabelFrame(self.container, text = 'Datos')
        self.containerEntries.grid(row = 2, column = 0, rowspan = 1, columnspan = 3, sticky = "e,w", ipadx = 10)

        self.NumIntervLbl = ttk.Label(self.containerEntries, text = "Numero de intervalos:")
        self.NumIntervLbl.grid(row = 0, column = 0)

        self.NumInterv = ttk.Entry(self.containerEntries, width = 15)
        self.NumInterv.grid(row = 0, column = 1, pady = 5)

        self.NumIntervLbl = ttk.Label(self.containerEntries, text = "valor:")
        self.NumIntervLbl.grid(row = 1, column =0, padx =10)

        self.NumInterv = ttk.Entry(self.containerEntries, width = 30)
        self.NumInterv.grid(row = 1, column = 1, columnspan = 2, padx =10)

        self.btnAggInterv = ttk.Button(self.containerEntries, text = "Agregar")
        self.btnAggInterv.grid(row = 1, column = 3, padx =10)

        self.btnCalc = ttk.Button(self.containerEntries, text = "Calcular")
        self.btnCalc.grid(row = 1, column = 4, padx =10)

        #TextArea values
        self.container_val = ttk.LabelFrame(self.container, text = 'valores')
        self.container_val.grid(row = 0, column = 0, rowspan = 2, sticky = "sw,nw,n,s,w", ipadx = 5)

        self.valuesTxt = Text(self.container_val, width = 25)
        self.valuesTxt.grid(row = 0, sticky = "sw,nw,n,s,w", padx = 5)
        self.valuesTxt["state"] = "disabled"
    
        self.scrollbar = ttk.Scrollbar(self.container_val)
        self.scrollbar.grid(row = 0, sticky = "e, n, s")

        self.valuesTxt.config( yscrollcommand = self.scrollbar.set )
        self.scrollbar.config( command = self.valuesTxt.yview )

        #frequence table
        self.containerTable = ttk.LabelFrame(self.container, text = 'tabla de frecuencia')
        self.containerTable.grid(row = 0, column = 1, columnspan = 2, sticky = "n, s, e, w")

        self.freqTable = ttk.Treeview(self.containerTable, height = 10, columns =('#1', '#2', '#3', '#4', '#5', '#6'))
        self.freqTable['show'] = 'headings'
        self.freqTable.heading('#1', text = "intervalos", anchor = CENTER)
        self.freqTable.heading('#2', text = "M", anchor = CENTER)
        self.freqTable.heading('#3', text = "f", anchor = CENTER)
        self.freqTable.heading('#4', text = "F", anchor = CENTER)
        self.freqTable.heading('#5', text = "Fr", anchor = CENTER)
        self.freqTable.heading('#6', text = "F%", anchor = CENTER)
        
        self.freqTable.column("#1", width = 150)
        self.freqTable.column("#2", width = 80)
        self.freqTable.column("#3", width = 80)
        self.freqTable.column("#4", width = 80)
        self.freqTable.column("#5", width = 80)
        self.freqTable.column("#6", width = 80)
        
        self.freqTable.grid(row = 0, column = 0, sticky = "n, e, w, s")

        #result container
        self.containerResult = ttk.LabelFrame(self.container, text = 'Resultados')
        self.containerResult.grid(row = 1, column = 1, sticky = "n,s,e,w")
        self.ResultTxt = Text(self.containerResult, height = 10, width = 67)
        self.ResultTxt.grid(row = 0, sticky = "w, n, s, e")
        self.ResultTxt["state"] = "disabled"
    
        self.scrollbar2 = ttk.Scrollbar(self.containerResult)
        self.scrollbar2.grid(row = 0, sticky = "e, n, s")

        self.ResultTxt.config( yscrollcommand = self.scrollbar2.set )
        self.scrollbar2.config( command = self.ResultTxt.yview )