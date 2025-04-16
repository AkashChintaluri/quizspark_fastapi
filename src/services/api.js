// Get the API URL based on environment
const getApiUrl = () => {
    if (process.env.NODE_ENV === 'production') {
        // In production, use the deployed backend URL
        return 'https://your-backend-domain.com/api';
    }
    // In development, use localhost
    return 'http://localhost:8000/api';
};

const API_BASE_URL = getApiUrl();

// Helper function to handle API requests
const apiRequest = async (endpoint, options = {}) => {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            ...options,
            headers: {
                'Content-Type': 'application/json',
                ...options.headers,
            },
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Something went wrong');
        }

        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
};

// Auth endpoints
export const auth = {
    signup: async (userData) => {
        return apiRequest('/signup', {
            method: 'POST',
            body: JSON.stringify(userData),
        });
    },
    login: async (credentials) => {
        return apiRequest('/login', {
            method: 'POST',
            body: JSON.stringify(credentials),
        });
    },
};

// Quiz endpoints
export const quizzes = {
    create: async (quizData) => {
        return apiRequest('/quizzes', {
            method: 'POST',
            body: JSON.stringify(quizData),
        });
    },
    getByCode: async (quizCode) => {
        return apiRequest(`/quizzes/${quizCode}`);
    },
    submitAttempt: async (quizCode, attemptData) => {
        return apiRequest(`/quizzes/${quizCode}/attempt`, {
            method: 'POST',
            body: JSON.stringify(attemptData),
        });
    },
};

// User endpoints
export const users = {
    getProfile: async () => {
        return apiRequest('/profile');
    },
    getSubscriptions: async () => {
        return apiRequest('/subscriptions');
    },
    subscribe: async (teacherId) => {
        return apiRequest('/subscriptions', {
            method: 'POST',
            body: JSON.stringify({ teacher_id: teacherId }),
        });
    },
}; 