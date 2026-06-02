import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
    ResponsiveContainer
} from 'recharts'

function AnalyticsChart({ data }) {

    if (!data || data.length === 0) {
        return null
    }

    const keys = Object.keys(data[0])

    const xAxisKey = keys[0]
    const valueKey = keys[1]

    return (
        <div style={{ marginTop: '30px' }}>

            <h2>Analytics Chart</h2>

            <ResponsiveContainer
                width="100%"
                height={400}
             >

                <BarChart data={data}>
                    <CartesianGrid />

                    <XAxis dataKey={xAxisKey} />

                    <YAxis />

                    <Tooltip />

                    <Bar dataKey={valueKey} />

                </BarChart>



            </ResponsiveContainer>
        </div>
    )
}

export default AnalyticsChart