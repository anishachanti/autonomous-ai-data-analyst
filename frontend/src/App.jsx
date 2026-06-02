import { useState } from 'react'
import axios from 'axios'
import AnalyticsChart from './components/AnalyticsChart'

function App() {

  const [file, setFile] = useState(null)

  const [analysis, setAnalysis] = useState(null)

  // const [preview, setPreview] = useState(null)

  const [question, setQuestion] = useState('')

  const [aiResponse, setAiResponse] = useState('')

  const [sqlQuestion, setSqlQuestion] = useState('')

  const [queryResults, setQueryResults] = useState([])

  const [chartData, setChartData] = useState([])

  const [chartPath, setChartPath] = useState('')

  const [insight, setInsight] = useState('')

  // const [generatedSQL, setGeneratedSQL] = useState('')

  const uploadFile = async () => {

    const formData = new FormData()

    formData.append('file', file)

    try {

      // Upload file
      await axios.post(
        'http://127.0.0.1:8000/upload',
        formData
      )

      // Preview API
      // const previewResponse = await axios.get(
      //   `http://127.0.0.1:8000/preview/${file.name}`
      // )
      //
      // setPreview(previewResponse.data)

      // Analyze API
      const analysisResponse = await axios.get(
        `http://127.0.0.1:8000/analyze/${file.name}`
      )

      setAnalysis(analysisResponse.data)

      alert('File uploaded successfully')

    } catch (error) {

      console.log(error)

      alert('Error uploading file')
    }
  }

  const askAI = async () => {

      if(!question){
          alert('Please enter a question')
          return
      }
      try {

          const response = await axios.post(
              `http://127.0.0.1:8000/chat/${file.name}`,

              {
                  question
              }
          )

          setAiResponse(response.data.response)
      } catch(error){

          console.log(error)

          alert('Error communicating with AI')
      }
  }

  const runAnalyticsQuery = async () => {

      if(!sqlQuestion) {
          alert('Please enter analytical question')
          return
      }

      try {

          const response = await axios.post(

              `http://127.0.0.1:8000/agent-query/${file.name}`,

              {
                  question: sqlQuestion
              }
          )

          console.log("FULL RESPONSE:")
          console.log(response.data)

          // setGeneratedSQL(response.data.generated_sql)

                  if (response.data.results) {

            setQueryResults(response.data.results)
            setChartData(response.data.results)

        }

                if (response.data.forecast) {

                    const forecastData = Array.isArray(response.data.forecast)
                        ? response.data.forecast
                        : [response.data.forecast]

                    setQueryResults(forecastData)
                    setChartData(forecastData)

                }

                if (response.data.insight) {

                    setInsight(
                        typeof response.data.insight === 'string'
                        ? response.data.insight
                        : JSON.stringify(response.data.insight)
                    )

                }
          if(response.data.chart){
              setChartPath(
        `http://127.0.0.1:8000/${response.data.chart.chart_path}`
              )
          }
      } catch(error) {
          console.log(error)

          alert('Error running analytics query')
      }
  }

  return (

    <div style={{ padding: '30px' }}>

      <h1>Autonomous AI Data Analyst</h1>

      {/* File Upload */}

      <div style={{ marginTop: '20px' }}>

        <input
          type='file'
          onChange={(e) => setFile(e.target.files[0])}
        />

        <br /><br />

        <button onClick={uploadFile}>
          Upload Dataset
        </button>

      </div>

      {/*/!* Dataset Preview *!/*/}

      {/*{*/}
      {/*  preview && (*/}

      {/*    <div style={{ marginTop: '40px' }}>*/}

      {/*      <h2>Dataset Preview</h2>*/}

      {/*      <table border='1' cellPadding='10'>*/}

      {/*        <thead>*/}

      {/*          <tr>*/}

      {/*            {*/}
      {/*              preview.columns.map((column) => (*/}

      {/*                <th key={column}>*/}
      {/*                  {column}*/}
      {/*                </th>*/}

      {/*              ))*/}
      {/*            }*/}

      {/*          </tr>*/}

      {/*        </thead>*/}

      {/*        <tbody>*/}

      {/*          {*/}
      {/*            preview.rows.map((row, index) => (*/}

      {/*              <tr key={index}>*/}

      {/*                {*/}
      {/*                  preview.columns.map((column) => (*/}

      {/*                    <td key={column}>*/}
      {/*                      {String(row[column])}*/}
      {/*                    </td>*/}

      {/*                  ))*/}
      {/*                }*/}

      {/*              </tr>*/}

      {/*            ))*/}
      {/*          }*/}

      {/*        </tbody>*/}

      {/*      </table>*/}

      {/*    </div>*/}
      {/*  )*/}
      {/*}*/}

      {/*/!* Dataset Analysis *!/*/}

      {/*{*/}
      {/*  analysis && (*/}

      {/*    <div style={{ marginTop: '40px' }}>*/}

      {/*      <h2>Dataset Analysis</h2>*/}

      {/*      <p>*/}
      {/*        <strong>Rows:</strong> {analysis.shape.rows}*/}
      {/*      </p>*/}

      {/*      <p>*/}
      {/*        <strong>Columns:</strong> {analysis.shape.columns}*/}
      {/*      </p>*/}

      {/*      <h3>Column Types</h3>*/}

      {/*      <ul>*/}

      {/*        {*/}
      {/*          Object.entries(analysis.dtypes).map(*/}

      {/*            ([column, dtype]) => (*/}

      {/*              <li key={column}>*/}
      {/*                {column}: {dtype}*/}
      {/*              </li>*/}
      {/*            )*/}
      {/*          )*/}
      {/*        }*/}

      {/*      </ul>*/}

      {/*      <h3>Missing Values</h3>*/}

      {/*      <ul>*/}

      {/*        {*/}
      {/*          Object.entries(analysis.missing_values).map(*/}

      {/*            ([column, value]) => (*/}

      {/*              <li key={column}>*/}
      {/*                {column}: {value}*/}
      {/*              </li>*/}
      {/*            )*/}
      {/*          )*/}
      {/*        }*/}

      {/*      </ul>*/}

      {/*      <h3>Numeric Columns</h3>*/}

      {/*      <ul>*/}

      {/*        {*/}
      {/*          analysis.numeric_columns.map((column) => (*/}

      {/*            <li key={column}>*/}
      {/*              {column}*/}
      {/*            </li>*/}

      {/*          ))*/}
      {/*        }*/}

      {/*      </ul>*/}

      {/*      <h3>Categorical Columns</h3>*/}

      {/*      <ul>*/}

      {/*        {*/}
      {/*          analysis.categorical_columns.map((column) => (*/}

      {/*            <li key={column}>*/}
      {/*              {column}*/}
      {/*            </li>*/}

      {/*          ))*/}
      {/*        }*/}

      {/*      </ul>*/}

      {/*    </div>*/}
      {/*  )*/}
      {/*}*/}

       {/* Dataset Summary */}

{
  analysis && (

    <div
      style={{
        marginTop: '40px',
        border: '1px solid #ccc',
        padding: '20px',
        borderRadius: '10px',
        width: '400px'
      }}
    >

      <h2>Dataset Loaded</h2>

      <p>
        <strong>Rows:</strong> {analysis.shape.rows}
      </p>

      <p>
        <strong>Columns:</strong> {analysis.shape.columns}
      </p>

      <p>
        <strong>Numeric Columns:</strong> {
          analysis.numeric_columns.length
        }
      </p>

      <p>
        <strong>Categorical Columns:</strong> {
          analysis.categorical_columns.length
        }
      </p>

    </div>
  )
}

      {/* AI Chat */}

      <div style={{ marginTop: '50px' }}>

        <h2>Ask AI</h2>

        <textarea
          rows='5'
          cols='60'
          placeholder='Ask questions about your dataset'
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <br /><br />

        <button onClick={askAI}>
          Ask AI
        </button>

        {
          aiResponse && (

            <div style={{ marginTop: '20px' }}>

              <h3>AI Response</h3>

              <div
                style={{
                  border: '1px solid gray',
                  padding: '15px',
                  borderRadius: '10px'
                }}
              >
                {aiResponse}
              </div>

            </div>
          )
        }

      </div>


      {
  chartPath && (

    <div style={{ marginTop: '20px' }}>

      <h3>Generated Chart</h3>

      <img
        src={chartPath}
        alt="chart"
        style={{
          width: '700px',
          border: '1px solid #ccc'
        }}
      />

    </div>

  )
}

      {/* SQL Analytics */}

      <div style={{ marginTop: '50px' }}>

        <h2>SQL Analytics</h2>

        <textarea
          rows='4'
          cols='60'
          placeholder='Ask analytical questions'
          value={sqlQuestion}
          onChange={(e) => setSqlQuestion(e.target.value)}
        />

        <br /><br />

        <button onClick={runAnalyticsQuery}>
          Run Analytics Query
        </button>

        {/*{*/}
        {/*  generatedSQL && (*/}

        {/*    <div style={{ marginTop: '20px' }}>*/}

        {/*      <h3>Generated SQL</h3>*/}

        {/*      <pre*/}
        {/*        style={{*/}
        {/*          backgroundColor: '#f4f4f4',*/}
        {/*          padding: '15px',*/}
        {/*          borderRadius: '10px'*/}
        {/*        }}*/}
        {/*      >*/}
        {/*        {generatedSQL}*/}
        {/*      </pre>*/}

        {/*    </div>*/}
        {/*  )*/}
        {/*}*/}

        {
          queryResults.length > 0 && (

            <div style={{ marginTop: '20px' }}>

              <h3>Query Results</h3>

              <table border='1' cellPadding='10'>

                <thead>

                  <tr>

                    {
                      Object.keys(queryResults[0]).map((column) => (

                        <th key={column}>
                          {column}
                        </th>

                      ))
                    }

                  </tr>

                </thead>

                <tbody>

                  {
                    queryResults.map((row, index) => (

                      <tr key={index}>

                        {
                          Object.values(row).map((value, i) => (

                            <td key={i}>
                              {String(value)}
                            </td>

                          ))
                        }

                      </tr>

                    ))
                  }

                </tbody>

              </table>

            </div>
          )
        }

        <AnalyticsChart data={chartData} />

{
  insight && (

    <div
      style={{
        marginTop: '20px',
        padding: '15px',
        border: '1px solid #ccc',
        borderRadius: '10px'
      }}
    >

      <h3>AI Insight</h3>

      <p>{insight}</p>

    </div>

  )
}

      </div>

    </div>

  )
}

export default App




