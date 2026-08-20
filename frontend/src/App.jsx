import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Activity, ShieldAlert, TrendingUp, Users, AlertCircle } from 'lucide-react';

const API_BASE_URL = 'http://localhost:8000';

function App() {
  const [status, setStatus] = useState('Checking...');
  const [riskData, setRiskData] = useState({
    debt_to_income: 0.3,
    payment_history: 0.8,
    utilization_ratio: 0.4
  });
  const [scoreResult, setScoreResult] = useState(null);

  useEffect(() => {
    axios.get(`${API_BASE_URL}/health`)
      .then(res => setStatus(res.data.status))
      .catch(() => setStatus('Offline'));
  }, []);

  const handleScore = async () => {
    try {
      const res = await axios.post(`${API_BASE_URL}/score/customer`, riskData);
      setScoreResult(res.data);
    } catch (err) {
      console.error(err);
      alert('Error calculating score');
    }
  };

  return (
    <div className="min-h-screen p-8">
      <header className="mb-8 flex justify-between items-center bg-white p-6 rounded-lg shadow-sm">
        <div>
          <h1 className="text-3xl font-bold text-gray-800">Finance Data Science</h1>
          <p className="text-gray-500">Risk Analysis & Forecasting Dashboard</p>
        </div>
        <div className="flex items-center gap-2">
          <div className={`h-3 w-3 rounded-full ${status === 'healthy' ? 'bg-green-500' : 'bg-red-500'}`}></div>
          <span className="font-medium text-gray-700">API Status: {status}</span>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <StatCard icon={<ShieldAlert className="text-red-500" />} title="Fraud Detection" value="Active" />
        <StatCard icon={<TrendingUp className="text-blue-500" />} title="Market Forecast" value="+2.4%" />
        <StatCard icon={<Users className="text-purple-500" />} title="Customer Segments" value="5 Groups" />
        <StatCard icon={<Activity className="text-orange-500" />} title="Anomalies" value="0 Detected" />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <section className="bg-white p-6 rounded-lg shadow-sm">
          <h2 className="text-xl font-semibold mb-6 flex items-center gap-2">
            <AlertCircle className="text-blue-600" />
            Customer Risk Scorer
          </h2>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700">Debt to Income Ratio</label>
              <input
                type="range" min="0" max="1" step="0.1"
                value={riskData.debt_to_income}
                onChange={e => setRiskData({...riskData, debt_to_income: parseFloat(e.target.value)})}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
              />
              <span className="text-xs text-gray-500">{riskData.debt_to_income}</span>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Payment History Score</label>
              <input
                type="range" min="0" max="1" step="0.1"
                value={riskData.payment_history}
                onChange={e => setRiskData({...riskData, payment_history: parseFloat(e.target.value)})}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
              />
              <span className="text-xs text-gray-500">{riskData.payment_history}</span>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Utilization Ratio</label>
              <input
                type="range" min="0" max="1" step="0.1"
                value={riskData.utilization_ratio}
                onChange={e => setRiskData({...riskData, utilization_ratio: parseFloat(e.target.value)})}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
              />
              <span className="text-xs text-gray-500">{riskData.utilization_ratio}</span>
            </div>
            <button
              onClick={handleScore}
              className="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition"
            >
              Calculate Risk Score
            </button>
          </div>

          {scoreResult && (
            <div className="mt-6 p-4 bg-gray-50 rounded-md border border-gray-100">
              <p className="text-sm text-gray-600">Calculated Score: <span className="font-bold text-gray-900">{scoreResult.score.toFixed(2)}</span></p>
              <p className="text-sm text-gray-600">Risk Tier: <span className={`font-bold ${scoreResult.risk_tier === 'High' ? 'text-red-600' : 'text-green-600'}`}>{scoreResult.risk_tier}</span></p>
            </div>
          )}
        </section>

        <section className="bg-white p-6 rounded-lg shadow-sm flex items-center justify-center border-2 border-dashed border-gray-200">
          <p className="text-gray-400">Additional Models & Charts Coming Soon...</p>
        </section>
      </div>
    </div>
  );
}

function StatCard({ icon, title, value }) {
  return (
    <div className="bg-white p-6 rounded-lg shadow-sm flex items-center gap-4">
      <div className="p-3 bg-gray-50 rounded-full">{icon}</div>
      <div>
        <p className="text-sm text-gray-500">{title}</p>
        <p className="text-2xl font-bold text-gray-800">{value}</p>
      </div>
    </div>
  );
}

export default App;
