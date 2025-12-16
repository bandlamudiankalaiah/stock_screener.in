// ==================== SCREEN BUILDER ====================

function addCriterion(existing = null) {
    const container = document.getElementById('criteriaContainer');
    const row = document.createElement('div');
    row.className = 'criteria-row';
    
    const metricsOptions = Object.keys(METRICS).map(key => 
        `<option value="${key}" ${existing && existing.metric === key ? 'selected' : ''}>
            ${METRICS[key].label}
        </option>`
    ).join('');
    
    const operatorOptions = {
        'number': `
            <option value="greater_than" ${existing && existing.operator === 'greater_than' ? 'selected' : ''}>&gt; Greater than</option>
            <option value="less_than" ${existing && existing.operator === 'less_than' ? 'selected' : ''}>&lt; Less than</option>
            <option value="equals" ${existing && existing.operator === 'equals' ? 'selected' : ''}>= Equals</option>
            <option value="between" ${existing && existing.operator === 'between' ? 'selected' : ''}>Between (e.g., 10-20)</option>
        `,
        'string': `
            <option value="equals" ${existing && existing.operator === 'equals' ? 'selected' : ''}>Equals</option>
            <option value="contains" ${existing && existing.operator === 'contains' ? 'selected' : ''}>Contains</option>
        `,
        'percentage': `
            <option value="greater_than" ${existing && existing.operator === 'greater_than' ? 'selected' : ''}>&gt; Greater than</option>
            <option value="less_than" ${existing && existing.operator === 'less_than' ? 'selected' : ''}>&lt; Less than</option>
        `
    };
    
    row.innerHTML = `
        <select onchange="updateOperators(this)">${metricsOptions}</select>
        <select class="operator-select">${operatorOptions.number}</select>
        <input type="text" placeholder="Value" value="${existing ? existing.value : ''}" onkeyup="handleEnter(event, this)">
        <button class="btn-remove" onclick="this.parentElement.remove()">✕</button>
    `;
    
    container.appendChild(row);
    
    // Set initial operator options based on metric type
    if (existing) {
        const metricType = METRICS[existing.metric].type;
        row.querySelector('.operator-select').innerHTML = operatorOptions[metricType];
    }
}

function updateOperators(metricSelect) {
    const row = metricSelect.parentElement;
    const operatorSelect = row.querySelector('.operator-select');
    const metric = metricSelect.value;
    const type = METRICS[metric].type;
    
    const options = {
        'number': `
            <option value="greater_than">&gt; Greater than</option>
            <option value="less_than">&lt; Less than</option>
            <option value="equals">= Equals</option>
            <option value="between">Between (e.g., 10-20)</option>
        `,
        'string': `
            <option value="equals">Equals</option>
            <option value="contains">Contains</option>
        `,
        'percentage': `
            <option value="greater_than">&gt; Greater than</option>
            <option value="less_than">&lt; Less than</option>
        `
    };
    
    operatorSelect.innerHTML = options[type];
}

function handleEnter(event, input) {
    if (event.key === 'Enter') {
        addCriterion();
    }
}

// ==================== SAVE & TEST ====================

function gatherCriteria() {
    const rows = document.querySelectorAll('.criteria-row');
    const criteria = [];
    
    rows.forEach(row => {
        const selects = row.querySelectorAll('select');
        const input = row.querySelector('input');
        if (selects[0].value && selects[1].value && input.value) {
            criteria.push({
                metric: selects[0].value,
                operator: selects[1].value,
                value: input.value
            });
        }
    });
    
    return criteria;
}

async function saveScreen() {
    const name = document.getElementById('screenName').value;
    const criteria = gatherCriteria();
    
    if (!name) {
        alert('Please enter a screen name');
        return;
    }
    
    if (criteria.length === 0) {
        alert('Please add at least one criterion');
        return;
    }
    
    const url = MODE === 'edit' ? `/screen/${SCREEN_DATA.id}/edit` : '/screen/create';
    const method = MODE === 'edit' ? 'PUT' : 'POST';
    
    try {
        const response = await fetch(url, {
            method: method,
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({name, criteria})
        });
        
        if (response.ok) {
            alert('Screen saved successfully!');
            window.location.href = '/';
        } else {
            alert('Failed to save screen');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function testScreen() {
    const criteria = gatherCriteria();
    if (criteria.length === 0) {
        alert('Please add at least one criterion');
        return;
    }
    
    try {
        const response = await fetch('/api/stocks/filter', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({criteria})
        });
        
        const stocks = await response.json();
        displayTestResults(stocks);
    } catch (error) {
        console.error('Error testing screen:', error);
    }
}

function displayTestResults(stocks) {
    const resultsDiv = document.getElementById('testResults');
    const tbody = resultsDiv.querySelector('tbody');
    
    resultsDiv.style.display = 'block';
    document.getElementById('resultCount').textContent = stocks.length;
    
    tbody.innerHTML = stocks.map(stock => `
        <tr>
            <td><strong>${stock.symbol}</strong></td>
            <td>${stock.name}</td>
            <td><span class="sector-tag">${stock.sector}</span></td>
            <td>${(stock.market_cap/1000).toFixed(1)}K</td>
            <td>₹${stock.current_price}</td>
            <td>${stock.pe_ratio || 'N/A'}</td>
            <td class="${stock.roe > 15 ? 'positive' : 'negative'}">${stock.roe}%</td>
            <td class="${stock.roce > 15 ? 'positive' : 'negative'}">${stock.roce}%</td>
        </tr>
    `).join('');
    
    // Scroll to results
    resultsDiv.scrollIntoView({behavior: 'smooth'});
}

// ==================== DASHBOARD ====================

async function loadScreens() {
    try {
        const response = await fetch('/screens');
        const screens = await response.json();
        
        const screensList = document.getElementById('screensList');
        screensList.innerHTML = screens.map(screen => `
            <div class="screen-card" style="border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; border-radius: 5px;">
                <h3>${screen.name}</h3>
                <p style="color: #666; font-size: 13px;">
                    ${screen.criteria.map(c => `${METRICS[c.metric].label} ${c.operator.replace('_', ' ')} ${c.value}`).join(' AND ')}
                </p>
                <div style="margin-top: 10px;">
                    <button class="btn btn-primary btn-sm" onclick="applyScreen(${screen.id})">Apply</button>
                    <button class="btn btn-secondary btn-sm" onclick="editScreen(${screen.id})">Edit</button>
                    <button class="btn btn-danger btn-sm" onclick="deleteScreen(${screen.id})">Delete</button>
                </div>
            </div>
        `).join('');
        
        document.getElementById('screensModal').style.display = 'block';
    } catch (error) {
        console.error('Error loading screens:', error);
    }
}

function closeModal() {
    document.getElementById('screensModal').style.display = 'none';
}

async function applyScreen(screenId) {
    try {
        const response = await fetch(`/api/stocks/filter`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({screen_id: screenId})
        });
        
        const stocks = await response.json();
        updateDashboardTable(stocks);
        closeModal();
    } catch (error) {
        console.error('Error applying screen:', error);
    }
}

function editScreen(screenId) {
    window.location.href = `/screen/${screenId}/edit`;
}

async function deleteScreen(screenId) {
    if (!confirm('Are you sure you want to delete this screen?')) return;
    
    try {
        const response = await fetch(`/screen/${screenId}/delete`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            loadScreens(); // Refresh list
        }
    } catch (error) {
        console.error('Error deleting screen:', error);
    }
}

function updateDashboardTable(stocks) {
    const tbody = document.getElementById('stocksTableBody');
    const countP = document.getElementById('resultCount');
    
    tbody.innerHTML = stocks.map(stock => `
        <tr>
            <td><strong>${stock.symbol}</strong></td>
            <td>${stock.name}</td>
            <td><span class="sector-tag">${stock.sector}</span></td>
            <td>${(stock.market_cap/1000).toFixed(1)}K</td>
            <td>₹${stock.current_price}</td>
            <td>${stock.pe_ratio || 'N/A'}</td>
            <td>${stock.pb_ratio}</td>
            <td class="${stock.roe > 15 ? 'positive' : 'negative'}">${stock.roe}%</td>
            <td class="${stock.roce > 15 ? 'positive' : 'negative'}">${stock.roce}%</td>
            <td class="${stock.debt_to_equity < 1 ? 'positive' : 'negative'}">${stock.debt_to_equity}</td>
            <td class="${stock.revenue_growth > 10 ? 'positive' : 'negative'}">${stock.revenue_growth}%</td>
        </tr>
    `).join('');
    
    countP.textContent = `Showing ${stocks.length} stocks`;
}

function applyQuickFilter() {
    const sector = document.getElementById('sectorFilter').value;
    if (sector) {
        fetch('/api/stocks/filter', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({criteria: [{metric: 'sector', operator: 'equals', value: sector}]})
        })
        .then(r => r.json())
        .then(updateDashboardTable);
    } else {
        location.reload();
    }
}

async function exportData() {
    const criteria = []; // You can enhance this to export filtered data
    const csv = await fetch('/api/export', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({criteria})
    }).then(r => r.text());
    
    const blob = new Blob([csv], {type: 'text/csv'});
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `stock_screener_${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
}

// ==================== SEARCH FUNCTIONALITY ====================

let searchTimeout;

async function searchCompanies() {
    const input = document.getElementById('companySearch');
    const resultsDiv = document.getElementById('searchResults');
    const query = input.value.trim();
    
    clearTimeout(searchTimeout);
    
    if (query.length < 2) {
        resultsDiv.classList.remove('active');
        return;
    }
    
    searchTimeout = setTimeout(async () => {
        try {
            const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
            const results = await response.json();
            
            if (results.length === 0) {
                resultsDiv.innerHTML = '<div class="search-result-item" style="cursor: default;">No companies found</div>';
            } else {
                resultsDiv.innerHTML = results.map(stock => `
                    <div class="search-result-item" onclick="window.location.href='/company/${stock.symbol}'">
                        <div class="search-result-info">
                            <div class="search-result-symbol">${stock.symbol}</div>
                            <div class="search-result-name">${stock.name}</div>
                        </div>
                        <div class="search-result-price">
                            <div>₹${stock.current_price}</div>
                            <div style="font-size: 11px; color: #666;">${stock.sector}</div>
                        </div>
                    </div>
                `).join('');
            }
            
            resultsDiv.classList.add('active');
        } catch (error) {
            console.error('Search error:', error);
        }
    }, 300);
}

// Close search results when clicking outside
document.addEventListener('click', function(event) {
    const searchContainer = document.querySelector('.search-container');
    const resultsDiv = document.getElementById('searchResults');
    
    if (searchContainer && !searchContainer.contains(event.target)) {
        if (resultsDiv) {
            resultsDiv.classList.remove('active');
        }
    }
});

// ==================== THEME TOGGLE ====================

function toggleTheme() {
    const body = document.body;
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    if (currentTheme === 'light') {
        body.classList.add('dark-theme');
        localStorage.setItem('theme', 'dark');
    } else {
        body.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light');
    }
}

// Load saved theme on page load
document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
    }
});